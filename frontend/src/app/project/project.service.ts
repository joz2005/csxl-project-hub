import { Injectable, WritableSignal, computed, signal } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from '../authentication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable, tap } from 'rxjs';
import { Project } from './project.model';
import { PermissionService } from '../permission.service';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  private projectsSignal: WritableSignal<Project[]> = signal([]);
  projects = this.projectsSignal.asReadonly();

  constructor(
    protected http: HttpClient,
    protected auth: AuthenticationService,
    protected snackBar: MatSnackBar,
    protected permissionService: PermissionService
  ) {
    this.getProjects();
  }
  getProjects() {
    this.http.get<Project[]>('/api/projects').subscribe((projects) => {
      this.projectsSignal.set(projects);
    });
  }

  getProject(slug: string): Observable<Project | undefined> {
    return this.http.get<Project>('/api/projects/' + slug);
  }
}
