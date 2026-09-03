controle_notas = {}
alunos_aprovados = []

qtd_alunos = int(input("Enter the number of students: "))


def calculate_average(grades):
    """Calculate the average of the grades."""
    if not grades:
        return 0

    return sum(grades) / len(grades)


def check_approval(grade):
    """Check whether the student passed or failed."""
    if grade >= 7:
        return "Passed"

    return "Failed"


for i in range(qtd_alunos):

    name = input(f"Enter the name of student {i + 1}: ")
    grade = float(input(f"Enter the grade of student {i + 1}: "))

    controle_notas[name] = grade


print("\n=== Grade Control ===")

highest_grade = max(controle_notas.values())
lowest_grade = min(controle_notas.values())

for name, grade in controle_notas.items():

    status = check_approval(grade)

    print(
        f"Student: {name} | "
        f"Grade: {grade:.2f} | "
        f"Status: {status}"
    )

    if status == "Passed":
        alunos_aprovados.append(name)


average = calculate_average(list(controle_notas.values()))

print(f"\nClass average: {average:.2f}")


print("\n=== Highest Grade ===")

for name, grade in controle_notas.items():

    if grade == highest_grade:
        print(f"{name} - {grade:.2f}")


print("\n=== Lowest Grade ===")

for name, grade in controle_notas.items():

    if grade == lowest_grade:
        print(f"{name} - {grade:.2f}")


print("\n=== Approved Students ===")

for student in alunos_aprovados:
    print(student)
