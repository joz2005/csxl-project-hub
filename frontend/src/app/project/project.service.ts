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
  private recommendSignal: WritableSignal<Project[]> = signal([]);
  private projectsSignal: WritableSignal<Project[]> = signal([]);
  projects = this.projectsSignal.asReadonly();
  recommendations = this.recommendSignal.asReadonly();

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

  postResume(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('resume', file);

    return this.http.post<{ recommendations: Project[] }>(
      '/api/projects/recommendation',
      formData
    );
  }

  postApplication(project: Project): Observable<any> {
    return this.http.post('/api/projects/apply', project).pipe(
      tap(() => {
        this.snackBar.open('Application submitted successfully', 'Close', {
          duration: 2000
        });
      })
    );
  }
}
