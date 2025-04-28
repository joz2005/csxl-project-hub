import { Component, OnInit, computed } from '@angular/core';
import { ProjectService } from '../project.service';
import { Profile, ProfileService } from '../../profile/profile.service';


@Component({
  selector: 'job-applications-list',
  templateUrl: './job-applications-list.component.html',
  styleUrls: ['./job-applications-list.component.css']
})
export class JobApplicationsListComponent implements OnInit {
  public static Route = {
    path: '/projects/applications',
    title: 'Applications',
    component: JobApplicationsListComponent
  };

  applications = this.projectService.jobApplications;
  projects = this.projectService.projects;
  public profile: Profile;


  applicationProjects = computed(() => {
    const apps = this.applications();
    const projs = this.projects();
    return apps.map((app) => ({
      application: app,
      project: projs.find((p) => p.id === app.project_id)
    }));
  });

  constructor(private projectService: ProjectService, private profileService: ProfileService) {
    this.profile = this.profileService.profile()!;
  }

  ngOnInit() {
    this.projectService.getJobApplications();
  }
}
