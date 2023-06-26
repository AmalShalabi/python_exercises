from pathlib import Path
# path=Path("ecommerce")
# print(path.exists()) //True/False

# path=Path("emails")
# print(path.rmdir())
path=Path()
for file in path.glob('*.py'):
    print(file)