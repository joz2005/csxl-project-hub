import { Component, Input } from '@angular/core';
import { Project } from '../../project.model';
import { ApplyJob } from '../apply-job-dialog/apply-job-dialog.widget';
import { MatDialog } from '@angular/material/dialog';
import { Profile } from '../../../profile/profile.service';
import { ProjectService } from '../../project.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';

@Component({
  selector: 'project-details-info-card',
  templateUrl: './project-details-info-card.widget.html',
  styleUrls: ['./project-details-info-card.widget.css']
})
export class ProjectDetailsInfoCard {
  @Input() project: Project | undefined;
  @Input() profile!: Profile;


  showForm = false;

  constructor(
    private dialog: MatDialog,
    private projectService: ProjectService,
    private snackBar: MatSnackBar,
    private router: Router
    ) {}

  openApplyJobDialog(): void {
    const dialogRef = this.dialog.open(ApplyJob, {
      width: '1000px',
      autoFocus: false,
      maxWidth: 'none',
      data: { project: this.project }
    });
  }

  isAuthor(): boolean {
    if (!this.project || !this.profile) return false;
    return this.profile.id === this.project.author_id;
  }
  
  deleteProject(): void {
    if (!this.project) return;

    this.projectService.deleteProject(this.project.id!).subscribe({
      next: () => {
        this.snackBar.open('Project deleted', 'Close', { duration: 2000 });
        this.router.navigate(['/projects']);
      },
      error: (err) => {
        const message = err.error?.detail || err.message || 'Failed to delete project';
        this.snackBar.open(message, 'Close', { duration: 5000 });
      }
    });
  }
}
