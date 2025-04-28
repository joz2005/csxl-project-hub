import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProjectPageComponent } from './project-page/project-page.component';
import { ProjectDetailsComponent } from './project-details/project-details.component';
import { JobApplicationsListComponent } from './job-applications-list/job-applications-list.component';

const routes: Routes = [
  {
    path: '', // /projects               (project list)
    component: ProjectPageComponent,
    title: 'Projects'
  },
  {
    path: 'applications', // /projects/applications  (FULL page)
    component: JobApplicationsListComponent,
    title: 'Applications'
  },
  ProjectDetailsComponent.Route // /projects/:slug        (project details)
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProjectRoutingModule {}
