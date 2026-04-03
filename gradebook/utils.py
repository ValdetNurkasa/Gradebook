def parse_grade(value):
    try:
        grade = int(value)
    except ValueError:
        raise ValueError("Duhet numer...")
    
    if not (0 <= grade <=100):
        raise ValueError("0 - 100")
    
    return grade

def validate_empty(value, field_name="Value"):
    if not value.strip():
        raise ValueError(f"{field_name} Jo e that...")
    return value
    