"""Tests for the ProjectService class."""

import pytest
from unittest.mock import MagicMock, patch, create_autospec
import io

# Tested Dependencies
from backend.models import Project
from backend.services import ProjectService, PermissionService
from backend.services.exceptions import (
    UserPermissionException,
    ResourceNotFoundException,
)
from backend.models.resume import Resume

# Data Setup and Injected Service Fixtures
from backend.test.services.core_data import setup_insert_data_fixture
from backend.test.services.fixtures import project_svc_integration, permission_svc_mock
from backend.test.services.project.project_demo_data import (
    projects,
    conflicting_id_project,
    to_add,
)

# Data Models for Fake Data Inserted in Setup
from backend.test.services.user_data import root, user

__authors__ = ["Kamal Deep, Kaw Bu, Joseph Zheng, Zhi Yang"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


def test_get_all(project_svc_integration: ProjectService):
    """Test retrieving all projects."""
    fetched_projects = project_svc_integration.all()
    assert fetched_projects is not None
    assert len(fetched_projects) == len(projects)
    assert isinstance(fetched_projects[0], Project)


def test_get_by_slug(project_svc_integration: ProjectService):
    """Test retrieving project by slug."""
    slug = projects[0].slug
    project = project_svc_integration.get_by_slug(slug)
    assert project is not None
    assert isinstance(project, Project)
    assert project.slug == slug


def test_post_application_enforces_permission(project_svc_integration: ProjectService):
    """Test permission checks for project creation."""
    # Replace existing permission service with mock
    mock_permission = create_autospec(PermissionService)
    project_svc_integration._permission = mock_permission

    project_svc_integration.post_application(root, to_add)

    mock_permission.enforce.assert_called_once_with(
        root, "project.post_application", "project"
    )


def test_post_application_as_root(project_svc_integration: ProjectService):
    """Test root user can create project."""
    project = project_svc_integration.post_application(root, to_add)
    assert project is not None
    assert project.id is not None


def test_post_application_id_conflict(project_svc_integration: ProjectService):
    """Test ID conflict resolution."""
    project = project_svc_integration.post_application(root, conflicting_id_project)
    assert project is not None
    assert project.id != conflicting_id_project.id


def test_delete_permission_enforcement(project_svc_integration: ProjectService):
    """Test delete permission checks."""
    project = project_svc_integration.post_application(root, to_add)
    mock_permission = create_autospec(PermissionService)
    mock_permission.enforce.return_value = True
    project_svc_integration._permission = mock_permission
    project_svc_integration.remove_application(root, project.id)
    with pytest.raises(ResourceNotFoundException):
        project_svc_integration.get_by_slug(project.slug)


def test_regular_user_delete(project_svc_integration: ProjectService):
    """Test user permission enforcement."""
    with pytest.raises(ResourceNotFoundException):
        project_svc_integration.remove_application(user, projects[0].id)


def test_delete_nonexistent_project(project_svc_integration: ProjectService):
    """Test error handling for missing projects."""
    with pytest.raises(ResourceNotFoundException):
        project_svc_integration.remove_application(root, 9999)


def test_post_resume(project_svc_integration: ProjectService):
    """Test posting a resume."""
    mock_file = MagicMock()
    mock_file.file = io.BytesIO(b"Mock PDF content")
    mock_file.filename = "test_resume.pdf"

    with patch("PyPDF2.PdfReader") as mock_pdf_reader:
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "Test resume content"

        mock_reader = MagicMock()
        mock_reader.pages = [mock_page]
        mock_pdf_reader.return_value = mock_reader

        result = project_svc_integration.post_resume(mock_file)

        assert result is not None
        assert isinstance(result, Resume)
        assert result.content == "Test resume content"
        assert result.id is not None
