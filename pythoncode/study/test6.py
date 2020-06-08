import yaml

doc1="""
 a: 1
 b: 
    c: 3
    d: 4
"""

doc2="""
- a
- b
- c
"""
print(yaml.safe_load(doc1))
print(yaml.safe_load(doc2))