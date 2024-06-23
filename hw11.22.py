def replace(s, old, new):
    return new.join(s.split(old))

def test(condition):
    if condition:
        print("Test Passed!")
    else:
        print("Test Failed!")


test(replace("Mississippi", "i", "I") == "MIssIssIppI")
print(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
print(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
print(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
