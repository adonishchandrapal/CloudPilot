def recommend(project, provider):

    project = project.lower()

    if "blog" in project:
        return {
            "provider": provider,
            "frontend": "S3 Static Website",
            "backend": "EC2",
            "database": "RDS MySQL",
            "cost": "20$/month"
        }

    elif "ecommerce" in project:
        return {
            "provider": provider,
            "frontend": "CloudFront + S3",
            "backend": "EC2 Auto Scaling",
            "database": "RDS PostgreSQL",
            "cost": "100$/month"
        }

    elif "chat" in project:

        if provider == "AWS":
            return {
                "provider": provider,
                "frontend": "CloudFront",
                "backend": "ECS Containers",
                "database": "DynamoDB",
                "cost": "50$/month"
            }

        elif provider == "Azure":
            return {
                "provider": provider,
                "frontend": "Azure CDN",
                "backend": "Azure App Service",
                "database": "Azure Cosmos DB",
                "cost": "55$/month"
            }

        elif provider == "Google Cloud":
            return {
                "provider": provider,
                "frontend": "Cloud CDN",
                "backend": "Cloud Run",
                "database": "Firestore",
                "cost": "45$/month"
            }

    elif "video" in project:
        return {
            "provider": provider,
            "frontend": "CloudFront",
            "backend": "ECS Containers",
            "database": "DynamoDB",
            "cost": "200$/month"
        }

    else:
        return {
            "provider": provider,
            "frontend": "S3",
            "backend": "EC2",
            "database": "RDS",
            "cost": "10$/month"
        }