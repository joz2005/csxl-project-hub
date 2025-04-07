import { Component, OnInit } from '@angular/core';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  ResolveFn,
  Route
} from '@angular/router';

import { Project } from '../project.model';

@Component({
  selector: 'app-project-details',
  templateUrl: './project-details.component.html',
  styleUrl: './project-details.component.css'
})
export class ProjectDetailsComponent {
  public static Route: Route = {
    path: ':slug',
    component: ProjectDetailsComponent
  };

  public project!: Project;

  constructor(private route: ActivatedRoute) {
    const data = this.route.snapshot.data as {
      project: Project;
    };

    this.project = data.project;
  }
}
