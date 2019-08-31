from stp import db
from stp.models import users, startups
def main():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    main()

    user = users(username="pop",
                password="$2b$12$PcLzFFLFVewfN3ioArkNCOJjmVuMO7o4sluQgT.cf9uTvVUA2jO22",
                company="pop",
                phone_no="123",
                email="abc@abc.com")
    db.session.add(user)

# key = Key(key_no='91097412bfd2a0bf9cf9a6e8f78e3a7f')
# User_Byld.query.all()
