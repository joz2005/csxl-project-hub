/**
 * The Project Details Component enables applicants to view potential projects they might be interested in further detail.
 *
 * @author Zhi Hang Yang, Joseph Zheng, Kaw Bu, Kamal Deep Vasireddy
 * @copyright 2025
 * @license MIT
 */

import { Component } from '@angular/core';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  ResolveFn,
  Route
} from '@angular/router';
import { projectResolver } from '../project.resolver';
import { Project } from '../project.model';
import { Profile, ProfileService } from '../../profile/profile.service';

const titleResolver: ResolveFn<string> = (route: ActivatedRouteSnapshot) => {
  return route.parent!.data['project']?.title ?? 'Project Details';
};

@Component({
  selector: 'app-project-details',
  templateUrl: './project-details.component.html',
  styleUrls: ['./project-details.component.css']
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

  public project?: Project;
  public profile: Profile;

  constructor(
    private route: ActivatedRoute,
    private profileService: ProfileService
  ) {
    const data = this.route.snapshot.data as { project: Project };
    this.project = data.project;
    this.profile = this.profileService.profile()!;
  }
}
