from faker import Faker
faker = Faker("fa_IR")
######## GENERATE FAKE Variables ##########

fullname = faker.name()
username = faker.user_name()
password = faker.password()
email = faker.email()
job = faker.job()
address = faker.address()
favorite_color = faker.color_name()
website = faker.domain_name()


###### SHOW Fake Variables #########

print("Full Name :{}\n".format(fullname))
print("Username :{}\n".format(username))
print("Password :{}\n".format(password))
print("Email : {}\n".format(email))
print("Job :{}\n".format(job))
print("Address :{}\n".format(address.replace("\n","-")))
print("Favorite Color :{}\n".format(favorite_color))
print("Website :{}\n".format(website))
