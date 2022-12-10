from plane.db.models.project import ProjectIdentifier


def update_workspace_on_project_identifiers():
    """
    Back migration to migrate workspace in project identifiers
    """
    try:

        project_identifiers = ProjectIdentifier.objects.select_related("project").all()
        updated_project_identifiers = []

        for project_identifier in project_identifiers:
            project_identifier.workspace = project_identifier.project.workspace
            updated_project_identifiers.append(project_identifier)

        _ = ProjectIdentifier.objects.bulk_update(
            updated_project_identifiers, ["workspace"]
        )

        print("Success")
    except Exception as e:
        print(e)
        print("Failed")
