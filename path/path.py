from pathlib import Path


# print(dir(Path))

a=Path("D:\\2026\\python")
p=Path("path\\path.py")
print(a.exists())
print(p.exists())
t = p.is_dir()
t = p.is_file()
t = p.name
t = p.stem
t = p.suffix
t = p.absolute()
t = p.with_name("changed") 
t = p.with_suffix(".js")
print(t)

