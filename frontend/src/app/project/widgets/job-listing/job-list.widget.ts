import { Component, Input, ViewChild, TemplateRef } from '@angular/core';
import { JobApplication } from '../../job-application.model';
import { Project } from '../../project.model';
import { ProjectService } from '../../project.service';
import { Profile } from '../../../profile/profile.service';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'job-list',
  templateUrl: './job-list.widget.html',
  styleUrls: ['./job-list.widget.css']
})
export class JobList {
  @Input() application!: JobApplication;
  @Input() project?: Project;
  @Input() profile?: Profile;

  @ViewChild('contactDialog') contactDialog!: TemplateRef<any>;
  dialogRef!: MatDialogRef<any>;

  constructor(
    private projectService: ProjectService,
    private dialog: MatDialog
  ) {}

  acceptApplication(): void {
    // Open the contact info dialog
    this.dialogRef = this.dialog.open(this.contactDialog, {
      width: '400px',
      data: { contact: this.application.contact }
    });
  }

  confirmAccept(): void {
    // After confirming in the modal
    this.deleteApplication();
    this.dialogRef.close();
  }

  rejectApplication(): void {
    this.deleteApplication();
  }

  private deleteApplication(): void {
    if (this.application.id != null) {
      this.projectService.deleteJobApplication(this.application.id).subscribe({
        next: () => {
          console.log('Deleted successfully.');
          this.projectService.getJobApplications(); // Optional: refresh applications
        },
        error: (err) => {
          console.error('Failed to delete application:', err);
        }
      });
    } else {
      console.error('Cannot delete application: ID is null');
    }
  }

  isPoster(): boolean {
    return this.application?.poster_id === this.profile?.id;
  }

  isApplicant(): boolean {
    return this.application?.user_id === this.profile?.id;
  }
}
