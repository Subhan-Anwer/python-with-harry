# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

class Testing_self:
    def __init__(harry,name):
        harry.name = name
    def Say_Hello(harry):
        print(f"Hello Mr {harry.name}")
        
test = Testing_self("Subhan Sheikh")
test.Say_Hello()


# Yes you can!