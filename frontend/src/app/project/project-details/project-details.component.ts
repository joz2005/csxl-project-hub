import { Component, OnInit } from '@angular/core';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  ResolveFn,
  Route
} from '@angular/router';
import { projectResolver } from '../project.resolver';

import { Project } from '../project.model';

let titleResolver: ResolveFn<string> = (route: ActivatedRouteSnapshot) => {
  return route.parent!.data['project'].title;
};

@Component({
  selector: 'app-project-details',
  templateUrl: './project-details.component.html',
  styleUrl: './project-details.component.css'
})
export class ProjectDetailsComponent {
  public static Route: Route = {
    path: ':slug',
    component: ProjectDetailsComponent,
    resolve: {
      project: projectResolver
    },
    children: [
      {
        path: '',
        title: titleResolver,
        component: ProjectDetailsComponent
      }
    ]
  };

  public project: Project;

  constructor(private route: ActivatedRoute) {
    const data = this.route.snapshot.data as {
      project: Project;
    };

    this.project = data.project;
  }
}
