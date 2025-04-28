import { Component, Inject, inject, Input } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormBuilder, Validators } from '@angular/forms';
import { ProjectService } from '../../project.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Profile, ProfileService } from '../../../profile/profile.service';
import { ActivatedRoute } from '@angular/router';
import { Route } from '@angular/router';
import { profileResolver } from '../../../profile/profile.resolver';
import { Project } from '../../project.model';

@Component({
  selector: 'apply-job',
  templateUrl: './apply-job-dialog.widget.html',
  styleUrls: ['./apply-job-dialog.widget.css']
})
export class ApplyJob {
  public static Route: Route = {
    resolve: {
      profile: profileResolver
    }
  };

  profile: Profile;
  project: Project;

  constructor(
    public dialogRef: MatDialogRef<ApplyJob>,
    private projectService: ProjectService,
    private snackBar: MatSnackBar,
    private route: ActivatedRoute,
    private profileService: ProfileService,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    const profile_data = this.route.snapshot.data as {
      profile: Profile;
    };
    this.profile = this.profileService.profile()!;
    this.project = data.project;
  }

  private _formBuilder = inject(FormBuilder);

  jobForm = this._formBuilder.group({
    personal_statement: ['', Validators.required],
    experience: ['', Validators.required],
    gpa: ['', Validators.required],
    skills: ['', Validators.required],
    contact: ['', Validators.required]
  });

  get isValid(): boolean {
    return this.jobForm.valid;
  }

  close(): void {
    this.dialogRef.close();
  }

  submitJobApplication(): void {
    if (this.isValid) {
      const formValue = this.jobForm.value;

      const job_application = {
        id: Math.floor(Math.random() * 100),
        poster_id: this.project.author_id,
        user_id: this.profile.id,
        project_id: this.project.id,
        personal_statement: formValue.personal_statement,
        experience: formValue.experience,
        gpa: formValue.gpa,
        skills: formValue.skills,
        contact: formValue.skills
      };

      console.log(job_application);

      this.projectService.postJobApplication(job_application).subscribe({
        next: () => {
          this.snackBar.open('Applied to this project successfully', 'Close', {
            duration: 2000
          });
          this.dialogRef.close(job_application);
        },
        error: (error) => {
          this.snackBar.open(
            `Failed to Apply: ${error.error?.detail || 'Unknown error'}`,
            'Close',
            {
              duration: 5000
            }
          );
          console.error('Error creating job listing:', error);
        }
      });
    }
  }
}
