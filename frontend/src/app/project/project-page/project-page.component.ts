import { Component, Signal, effect } from '@angular/core';
import { Project } from '../project.model';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Profile, ProfileService } from '../../profile/profile.service';
import { NagivationAdminGearService } from '../../navigation/navigation-admin-gear.service';
import { ProjectService } from '../project.service';
import { AiResumeSearch } from '../widgets/ai-resume-search/ai-resume-search.widget';
import { MatDialog } from '@angular/material/dialog';
import { signal, computed } from '@angular/core';
import { AddJob } from '../widgets/add-job/add-job.widget';

@Component({
  selector: 'app-project',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.css']
})
export class ProjectPageComponent {
  public static Route = {
    path: '',
    title: 'Projects',
    component: ProjectPageComponent
  };

  uploadState = signal<{
    loading: boolean;
    error: string | null;
    data: Project[] | null;
  }>({
    loading: false,
    error: null,
    data: null
  });

  // Computed signals for template convenience
  isUploading = computed(() => this.uploadState().loading);
  uploadError = computed(() => this.uploadState().error);
  aiRecommendations = computed(() => this.uploadState().data || []);

  public searchBarQuery = '';
  public projects: Signal<Project[]>;
  public fileName = '';
  public profile: Profile;

  constructor(
    protected snackBar: MatSnackBar,
    private projectService: ProjectService,
    private gearService: NagivationAdminGearService,
    private profileService: ProfileService,
    private dialog: MatDialog
  ) {
    this.projects = this.projectService.projects;
    this.profile = this.profileService.profile()!;
  }

  recommendations = signal<Project[]>([]);
  isProcessing = signal(false);

  openResumeUploadModol(): void {
    const dialogRef = this.dialog.open(AiResumeSearch, {
      width: '1000px',
      autoFocus: false
    });

    dialogRef.afterClosed().subscribe((file: File | undefined) => {
      if (file) {
        this.isProcessing.set(true);
        this.fileName = file.name;

        const loadingSnackbar = this.snackBar.open(
          'Analyzing your resume with AI...',
          undefined,
          { duration: 0 }
        );

        this.projectService.postResume(file).subscribe({
          next: (response) => {
            this.recommendations.set(response.recommendations);
            loadingSnackbar.dismiss();
            console.log(response.listings[0].slug);

            const origin = window.location.origin;
            let rv: String = '';
            let most_fit: number = 1;
            response.listings.forEach((element: { title: string }) => {
              rv += `${most_fit}. ${element.title}` + ' ';
              most_fit += 1;
            });
            this.snackBar.open(
              response.message || 'Found matching projects! ' + rv,
              'Close',
              {
                duration: Infinity,
                panelClass: ['success-snackbar'],
                data: {
                  // Pass the recommendations to the snackbar
                  projects: response.recommendations
                }
              }
            );
          },
          error: (err) => {
            loadingSnackbar.dismiss();
            this.snackBar.open(
              err.error?.message || 'Failed to analyze resume',
              'Close',
              {
                duration: 5000,
                panelClass: ['error-snackbar']
              }
            );
          },
          complete: () => this.isProcessing.set(false)
        });
      }
    });
  }
  openAddJobModol(): void {
    const dialogRef = this.dialog.open(AddJob, {
      width: '1000px',
      autoFocus: false,
      maxWidth: 'none',
      data: { profile: this.profile }
    });
  }

  onDelete(projectId: number): void {
    this.projectService.deleteProject(projectId).subscribe({
      next: () => {
        this.snackBar.open('Project deleted', 'Close', { duration: 2000 });
      },
      error: (err) => {
        const message =
          err.error?.detail || err.message || 'Failed to delete project';
        this.snackBar.open(message, 'Close', { duration: 5000 });
      }
    });
  }
}
