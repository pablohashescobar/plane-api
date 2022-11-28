from django.urls import path


# Create your urls here.

from plane.api.views import (
    SignInEndpoint,
    SignOutEndpoint,
    MagicSignInEndpoint,
    MagicSignInGenerateEndpoint,
    ForgotPasswordEndpoint,
    PeopleEndpoint,
    UserEndpoint,
    VerifyEmailEndpoint,
    ResetPasswordEndpoint,
    RequestEmailVerificationEndpoint,
    OauthEndpoint,
    ChangePasswordEndpoint,
)

from plane.api.views import (
    UserWorkspaceInvitationsEndpoint,
    WorkSpaceViewSet,
    UserWorkSpacesEndpoint,
    InviteWorkspaceEndpoint,
    JoinWorkspaceEndpoint,
    WorkSpaceMemberViewSet,
    WorkspaceInvitationsViewset,
    UserWorkspaceInvitationsEndpoint,
    ProjectViewSet,
    InviteProjectEndpoint,
    ProjectMemberViewSet,
    ProjectMemberInvitationsViewset,
    StateViewSet,
    ShortCutViewSet,
    ViewViewSet,
    CycleViewSet,
    FileAssetEndpoint,
    IssueViewSet,
    UserIssuesEndpoint,
    WorkSpaceIssuesEndpoint,
    IssueActivityEndpoint,
    IssueCommentViewSet,
    TeamMemberViewSet,
    TimeLineIssueViewSet,
    CycleIssueViewSet,
    IssuePropertyViewSet,
    UpdateUserOnBoardedEndpoint,
    UserWorkspaceInvitationEndpoint,
    UserProjectInvitationsViewset,
    ProjectIdentifierEndpoint,
    LabelViewSet,
    AddMemberToProjectEndpoint,
    ProjectJoinEndpoint,
    BulkDeleteIssuesEndpoint,
)

from plane.api.views.project import AddTeamToProjectEndpoint


urlpatterns = [
    #  Social Auth
    path("social-auth/", OauthEndpoint.as_view(), name="oauth"),
    # Auth
    path("sign-in/", SignInEndpoint.as_view(), name="sign-in"),
    path("sign-out/", SignOutEndpoint.as_view(), name="sign-out"),
    # Magic Sign In/Up
    path(
        "magic-generate/", MagicSignInGenerateEndpoint.as_view(), name="magic-generate"
    ),
    path("magic-sign-in/", MagicSignInEndpoint.as_view(), name="magic-sign-in"),
    # Email verification
    path("email-verify/", VerifyEmailEndpoint.as_view(), name="email-verify"),
    path(
        "request-email-verify/",
        RequestEmailVerificationEndpoint.as_view(),
        name="request-reset-email",
    ),
    # Password Manipulation
    path(
        "password-reset/<uidb64>/<token>/",
        ResetPasswordEndpoint.as_view(),
        name="password-reset",
    ),
    path(
        "forgot-password/",
        ForgotPasswordEndpoint.as_view(),
        name="forgot-password",
    ),
    # List Users
    path("users/", PeopleEndpoint.as_view()),
    # User Profile
    path(
        "users/me/",
        UserEndpoint.as_view(
            {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
        ),
        name="users",
    ),
    path(
        "users/me/change-password/",
        ChangePasswordEndpoint.as_view(),
        name="change-password",
    ),
    path(
        "users/me/onboard/",
        UpdateUserOnBoardedEndpoint.as_view(),
        name="change-password",
    ),
    # user workspaces
    path(
        "users/me/workspaces/",
        UserWorkSpacesEndpoint.as_view(),
        name="user-workspace",
    ),
    # user workspace invitations
    path(
        "users/me/invitations/workspaces/",
        UserWorkspaceInvitationsEndpoint.as_view({"get": "list", "post": "create"}),
        name="user-workspace-invitations",
    ),
    # user workspace invitation
    path(
        "users/me/invitations/<uuid:pk>/",
        UserWorkspaceInvitationEndpoint.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="workspace",
    ),
    # user join workspace
    path(
        "users/me/invitations/workspaces/<str:slug>/<uuid:pk>/join/",
        JoinWorkspaceEndpoint.as_view(),
        name="user-join-workspace",
    ),
    # user project invitations
    path(
        "users/me/invitations/projects/",
        UserProjectInvitationsViewset.as_view({"get": "list", "post": "create"}),
        name="user-project-invitaions",
    ),
    # user issues
    path(
        "users/me/issues/",
        UserIssuesEndpoint.as_view(),
        name="user-issues",
    ),
    ## Workspaces ##
    path(
        "workspaces/",
        WorkSpaceViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/",
        WorkSpaceViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/invite/",
        InviteWorkspaceEndpoint.as_view(),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/invitations/",
        WorkspaceInvitationsViewset.as_view({"get": "list"}),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/invitations/<uuid:pk>/",
        WorkspaceInvitationsViewset.as_view(
            {
                "delete": "destroy",
                "get": "retrieve",
                "get": "retrieve",
            }
        ),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/members/",
        WorkSpaceMemberViewSet.as_view({"get": "list"}),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/members/<uuid:pk>/",
        WorkSpaceMemberViewSet.as_view(
            {
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
                "get": "retrieve",
            }
        ),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/teams/",
        TeamMemberViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/teams/<uuid:pk>/",
        TeamMemberViewSet.as_view(
            {
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
                "get": "retrieve",
            }
        ),
        name="workspace",
    ),
    ## End Workspaces ##
    # Projects
    path(
        "workspaces/<str:slug>/projects/",
        ProjectViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:pk>/",
        ProjectViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/project-identifiers/",
        ProjectIdentifierEndpoint.as_view(),
        name="project-identifiers",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/invite/",
        InviteProjectEndpoint.as_view(),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/members/",
        ProjectMemberViewSet.as_view({"get": "list"}),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/members/<uuid:pk>/",
        ProjectMemberViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/members/add/",
        AddMemberToProjectEndpoint.as_view(),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/projects/join/",
        ProjectJoinEndpoint.as_view(),
        name="project",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/team-invite/",
        AddTeamToProjectEndpoint.as_view(),
        name="projects",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/invitations/",
        ProjectMemberInvitationsViewset.as_view({"get": "list"}),
        name="workspace",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/invitations/<uuid:pk>/",
        ProjectMemberInvitationsViewset.as_view(
            {
                "get": "retrieve",
                "delete": "destroy",
            }
        ),
        name="project",
    ),
    #  States
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/states/",
        StateViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-states",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/states/<uuid:pk>/",
        StateViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-state",
    ),
    # End States ##
    # Shortcuts
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/shortcuts/",
        ShortCutViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-shortcut",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/shortcuts/<uuid:pk>/",
        ShortCutViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-shortcut",
    ),
    ## End Shortcuts
    # Views
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/views/",
        ViewViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-view",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/views/<uuid:pk>/",
        ViewViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-view",
    ),
    ## End Views
    ## Cycles
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/cycles/",
        CycleViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-cycle",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/cycles/<uuid:pk>/",
        CycleViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-cycle",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/cycles/<uuid:cycle_id>/cycle-issues/",
        CycleIssueViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-cycle",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/cycles/<uuid:cycle_id>/cycle-issues/<uuid:pk>/",
        CycleIssueViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-cycle",
    ),
    ## End Cycles
    # Issue
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/",
        IssueViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-issue",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/<uuid:pk>/",
        IssueViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-issue",
    ),
    path(
        "workspaces/<str:slug>/issues/",
        WorkSpaceIssuesEndpoint.as_view(),
        name="workspace-issue",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issue-labels/",
        LabelViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-issue-labels",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issue-labels/<uuid:pk>/",
        LabelViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-issue-labels",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/bulk-delete-issues/",
        BulkDeleteIssuesEndpoint.as_view(),
    ),
    ## End Issues
    ## Issue Activity
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/<uuid:issue_id>/history/",
        IssueActivityEndpoint.as_view(),
        name="project-issue-history",
    ),
    ## Issue Activity
    ## IssueComments
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/<uuid:issue_id>/comments/",
        IssueCommentViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-issue-comment",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/<uuid:issue_id>/comments/<uuid:pk>/",
        IssueCommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-issue-comment",
    ),
    ## End IssueComments
    ## Roadmap
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/<uuid:issue_id>/roadmaps/",
        TimeLineIssueViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-issue-roadmap",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issues/<uuid:issue_id>/roadmaps/<uuid:pk>/",
        TimeLineIssueViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-issue-roadmap",
    ),
    ## End Roadmap
    ## IssueProperty
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issue-properties/",
        IssuePropertyViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project-issue-roadmap",
    ),
    path(
        "workspaces/<str:slug>/projects/<uuid:project_id>/issue-properties/<uuid:pk>/",
        IssuePropertyViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="project-issue-roadmap",
    ),
    ## IssueProperty Ebd
    ## File Assets
    path(
        "file-assets/",
        FileAssetEndpoint.as_view(),
        name="File Assets",
    ),
    ## End File Assets
    # path(
    #     "issues/<int:pk>/all/",
    #     IssueViewSet.as_view({"get": "list_issue_history_comments"}),
    #     name="Issue history and comments",
    # ),
]
