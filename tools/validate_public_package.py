"""Public documentation integrity only; not scientific or legal certification."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
  'README.md', 'README_RU.md', 'LEGAL.md', 'SECURITY.md', 'CONTRIBUTING.md',
  '.gitignore', '.github/workflows/validate.yml',
  'tools/validate_public_package.py',
  'assets/kilu-hero.svg','assets/authority-flow.svg',
  'assets/kilu-logo.svg','assets/kilu-symbol.svg',
  'evidence/CLAIMS_REGISTER.csv', 'evidence/SOURCES.csv', 'evidence/INDEX.md',
  'docs/INDEX.md', 'docs/15_HOMEOSTATIC_EDGE_EVIDENCE.md',
  *{f'docs/{i:02d}_{suffix}.md' for i, suffix in enumerate([
    'START_HERE','EXECUTIVE_OVERVIEW','ARCHITECTURE_BOUNDARIES',
    'AEGISAI_GOVERNANCE','EXECUTION_EVIDENCE','APPROVAL_EVIDENCE',
    'REVIEW_PROTOCOL','DISCLOSURE_BOUNDARY','INTEGRATION_QUALIFICATION',
    'LIMITATIONS_AND_RISKS','COMMERCIAL_DILIGENCE','THREAT_MODEL',
    'PUBLIC_REPRODUCIBILITY','FAQ','DETERMINISTIC_GATE_EVIDENCE'
  ])},
}
actual = {
  str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
  if p.is_file() and '.git' not in p.parts
}
assert REQUIRED == actual, f'missing/unreviewed paths: {sorted(REQUIRED ^ actual)}'
def load(name):
  with (ROOT/name).open(newline='', encoding='utf-8') as handle:
    return list(csv.DictReader(handle))
sources = load('evidence/SOURCES.csv')
claims = load('evidence/CLAIMS_REGISTER.csv')
assert len(claims) >= 26 and len(sources) >= 10
source_ids = [s['source_id'] for s in sources]
claim_ids = [c['claim_id'] for c in claims]
assert len(source_ids) == len(set(source_ids)), 'duplicate source ID'
assert len(claim_ids) == len(set(claim_ids)), 'duplicate claim ID'
statuses = {
  'PUBLIC_CI_PASS','PUBLIC_SOURCE_OBSERVED','PASS_SCOPED_INTERNAL',
  'REPORTED_PREVIOUS_VALIDATION','SPECIFIED','NOT_ESTABLISHED',
  'PROSPECTIVE','OPEN_DECISION'
}
for c in claims:
  assert all(c.get(k) for k in ('claim_id','component','claim','status','scope','source_id','qualification'))
  assert c['status'] in statuses and c['source_id'] in source_ids, c['claim_id']
positive = {'KILU-08':'SPECIFIED','AEGIS-03':'PASS_SCOPED_INTERNAL','AEGIS-04':'PASS_SCOPED_INTERNAL','DET-01':'PASS_SCOPED_INTERNAL','APP-05':'PUBLIC_SOURCE_OBSERVED','APP-06':'SPECIFIED'}
for k, status in positive.items():
  assert any(c['claim_id']==k and c['status']==status for c in claims),f'no verified scope for {k}'
negative = {'APP-03','APP-04','KILU-06','KILU-07','CHAIN-01','CHAIN-02','SDK-02'}
by_id = {c['claim_id']:c for c in claims}
assert negative.issubset(by_id)
assert all(by_id[k]['status']=='NOT_ESTABLISHED' for k in negative)
for s in sources:
  assert s['access'] in ('PUBLIC','INTERNAL_ONLY')
  if s['access']=='INTERNAL_ONLY':
    assert not s['public_url'], s['source_id']
  else:
    assert s['public_url'].startswith((
      'https://github.com/IkaRiche/kilu-pocket-agent',
      'https://github.com/IkaRiche/kilu-sdk',
    )), s['source_id']
# Deliberately heuristic: always perform human disclosure review before publication.
patterns = [
  ('private GitHub repository',r'https?://github\.com/IkaRiche/(?:KiLu-Network|AegisAI)(?:[/#\s]|$)'),
  ('private key',r'-----BEGIN (?:[A-Z ]* )?PRIVATE KEY-----'),
  ('access token',r'\b(?:ghp_|gho_|github_pat_)\S+'),
  ('long SHA',r'\b[a-f0-9]{40}\b'),
  ('prospective buyer',r'\bNebius\b'),
]
for rel in actual:
  if rel == 'tools/validate_public_package.py':
    continue
  content = (ROOT/rel).read_text(encoding='utf-8')
  for label,pattern in patterns:
    assert not re.search(pattern,content,re.I), f'potential {label} in {rel}'
for md in ROOT.rglob('*.md'):
  content=md.read_text(encoding='utf-8')
  for target in re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)',content):
    relpath=target.split('#',1)[0]
    if not relpath or relpath.startswith(('https://','http://','mailto:','#')):
      continue
    resolved=(md.parent/relpath).resolve()
    assert resolved.is_relative_to(ROOT.resolve()) and resolved.is_file(),f'broken reference {md.relative_to(ROOT)}: {relpath}'
print(f'PUBLIC_PACKAGE_STRUCTURE_OK: {len(actual)} controlled files, {len(claims)} claims, {len(sources)} sources')
print('NOT scientific, security, IP or legal validation')
