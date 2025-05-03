/**
 * The Project Service abstracts HTTP requests to the backend
 * from the components.
 *
 * @author Zhi Hang Yang, Joseph Zheng, Kaw Bu, Kamal Deep Vasireddy
 * @copyright 2025
 * @license MIT
 */

import { Injectable, WritableSignal, computed, signal } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { AuthenticationService } from '../authentication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable, tap } from 'rxjs';
import { Project } from './project.model';
import { PermissionService } from '../permission.service';
import { JobApplication } from './job-application.model';

@Injectable({
  providedIn: 'root'
})
export class ProjectService {
  private recommendSignal: WritableSignal<Project[]> = signal([]);
  private projectsSignal: WritableSignal<Project[]> = signal([]);
  private jobApplicationsSignal: WritableSignal<any[]> = signal([]);
  jobApplications = this.jobApplicationsSignal.asReadonly();
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

  postJob(job: any): Observable<Project> {
    return this.http.post<Project>('/api/projects', job).pipe(
      tap((newProject) => {
        this.projectsSignal.update((projects) => [...projects, newProject]);
      })
    );
  }
  deleteProject(id: number) {
    return this.http.delete<void>(`/api/projects/${id}`).pipe(
      tap(() => {
        this.projectsSignal.update((projects) =>
          projects.filter((p) => p.id !== id)
        );
      })
    );
  }

  getJobApplications() {
    this.http
      .get<JobApplication[]>('/api/projects/job-applications')
      .subscribe((projects) => {
        this.jobApplicationsSignal.set(projects);
      });
  }

  postJobApplication(application: any): Observable<any> {
    return this.http
      .post<any>('/api/projects/job-applications', application) // <-- URL from Swagger
      .pipe(
        tap((newApplication) => {
          // keep local cache in sync (optional)
          this.jobApplicationsSignal.update((apps) => [
            ...apps,
            newApplication
          ]);
        })
      );
  }

  deleteJobApplication(id: number) {
    return this.http.delete(`/api/projects/job-applications/${id}`);
  }
}
