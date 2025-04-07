import { Component, Signal, effect } from '@angular/core';
import { Project } from '../project.model';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Profile, ProfileService } from '../../profile/profile.service';
import { NagivationAdminGearService } from '../../navigation/navigation-admin-gear.service';
import { ProjectService } from '../project.service';

@Component({
  selector: 'app-project',
  templateUrl: './project-page.component.html',
  styleUrl: './project-page.component.css'
})
export class ProjectPageComponent {
  public searchBarQuery = '';
  public projects: Signal<Project[]>;

  constructor(
    protected snackBar: MatSnackBar,
    private projectService: ProjectService,
    private gearService: NagivationAdminGearService
  ) {
    this.projects = this.projectService.projects;
  }
}
