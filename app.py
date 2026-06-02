# print("☁️ Welcome to CloudPilot")

# project = input("Tell about your project: ").lower()

# if "blog" in project:

#     provider = "AWS"

#     frontend = "S3 Static Website"
#     backend = "EC2"
#     database = "RDS MySQL"

# elif "ecommerce" in project:

#     provider = "AWS"

#     frontend = "CloudFront + S3"
#     backend = "EC2 Auto Scaling"
#     database = "RDS PostgreSQL"

# elif "chat" in project:

#     provider = "AWS"

#     frontend = "CloudFront"
#     backend = "ECS Containers"
#     database = "DynamoDB"

# else:

#     provider = "AWS"

#     frontend = "S3"
#     backend = "EC2"
#     database = "RDS"

# print("\n===== CLOUDPILOT REPORT =====")

# print("Cloud Provider:", provider)
# print("Frontend:", frontend)
# print("Backend:", backend)
# print("Database:", database)

# from cloud_recommender import recommend

# print("☁️ Welcome to CloudPilot")

# project = input("Tell about your project: ")
# with open("history.txt", "a") as file:
#     file.write(project + "\n")

# result = recommend(project)

# print("\n===== CLOUDPILOT REPORT =====")

# print("Cloud Provider:", result["provider"])
# print("Frontend:", result["frontend"])
# print("Backend:", result["backend"])
# print("Database:", result["database"])
# print("Estimated Cost:", result["cost"])

from cloud_recommender import recommend

while True:

    print("\n===== CLOUDPILOT =====")
    print("1. Get Recommendation")
    print("2. View History")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        project = input("Describe your application or project: ")

        users = int(input("Expected monthly users: "))

        with open("history.txt", "a") as file:
            file.write(project + "\n")

        result = recommend(project)

        print("\n===== CLOUDPILOT REPORT =====")
        print("Cloud Provider:", result["provider"])
        print("Frontend:", result["frontend"])
        print("Backend:", result["backend"])
        print("Database:", result["database"])
        print("Estimated Cost:", result["cost"])

        print("\nArchitecture Summary:")
        print(f"{result['frontend']} -> {result['backend']} -> {result['database']}")

        if users < 1000:
            scale = "Small"

        elif users < 10000:
            scale = "Medium"

        else:
            scale = "Large"

        print("Scale:", scale)

    elif choice == "2":

        try:
            with open("history.txt", "r") as file:
                print("\n===== HISTORY =====")
                print(file.read())

        except FileNotFoundError:
            print("No history found.")

    elif choice == "3":

        print("Thank you for using CloudPilot!")
        break

    else:
        print("Invalid option.")