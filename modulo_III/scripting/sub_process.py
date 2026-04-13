import subprocess

# subprocess.run(["ls", "-lart"])


hostname = subprocess.run(["hostname"], capture_output=True, encoding="cp850")

print("el nombre de mi pc es:", hostname.stdout)


python_version = subprocess.run(["python3", "--version"], capture_output=True, encoding="cp850")

print("la vesion de python es:", python_version.stdout)