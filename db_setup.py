from stp import db
from stp.models import User_Byld, Key

def main():
    db.create_all()
    db.session.commit()
    

if __name__ == "__main__":
    main()

# key = Key(key_no='91097412bfd2a0bf9cf9a6e8f78e3a7f')
# User_Byld.query.all()
