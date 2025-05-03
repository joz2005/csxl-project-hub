/**
 * The Add job Widgets provide a modol base interface for developers to upload their project.
 * It also seperates the implementation from the main project page, promoting decoupled code.
 *
 * @author Zhi Hang Yang, Joseph Zheng, Kaw Bu, Kamal Deep Vasireddy
 * @copyright 2025
 * @license MIT
 */

import { Component, inject, Input, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { FormBuilder, Validators } from '@angular/forms';
import { ProjectService } from '../../project.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Profile } from '../../../profile/profile.service';
import { ActivatedRoute } from '@angular/router';
import { Route } from '@angular/router';
import { profileResolver } from '../../../profile/profile.resolver';

@Component({
  selector: 'add-job',
  templateUrl: './add-job.widget.html',
  styleUrls: ['./add-job.widget.css']
})
export class AddJob {
  public static Route: Route = {
    resolve: {
      profile: profileResolver
    }
  };
  @Input() profile: Profile;

  constructor(
    public dialogRef: MatDialogRef<AddJob>,
    private projectService: ProjectService,
    private snackBar: MatSnackBar,
    private route: ActivatedRoute,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    this.profile = data.profile;
  }

  private _formBuilder = inject(FormBuilder);

  jobForm = this._formBuilder.group({
    project_name: ['', Validators.required],
    project_image: ['', Validators.required],
    long_description: ['', Validators.required],
    short_description: ['', Validators.required],
    requirements: ['', Validators.required],
    additional_info: [''],
    email: ['', [Validators.required, Validators.email]],
    phone_number: [''],
    linked_in: ['']
  });

  get isValid(): boolean {
    return this.jobForm.valid;
  }

  close(): void {
    this.dialogRef.close();
  }

  submitJob(): void {
    if (this.isValid) {
      const formValue = this.jobForm.value;
      // Create a unique slug by adding timestamp
      const timestamp = new Date().getTime();
      const uniqueSlug = `${formValue.project_name!.toLowerCase().replace(/ /g, '-')}`;

      const job = {
        id: Math.floor(Math.random() * 100),
        author_id: this.profile.id,
        author: this.profile.first_name + ' ' + this.profile.last_name,
        title: formValue.project_name,
        image: formValue.project_image,
        long_description: formValue.long_description,
        short_description: formValue.short_description,
        requirements: formValue.requirements,
        additional_info: formValue.additional_info,
        email: formValue.email,
        phone_number: formValue.phone_number,
        linked_in: formValue.linked_in,
        public: true,
        slug: uniqueSlug
      };

      this.projectService.postJob(job).subscribe({
        next: () => {
          this.snackBar.open('Job listing created successfully', 'Close', {
            duration: 2000
          });
          this.dialogRef.close(job);
        },
        error: (error) => {
          this.snackBar.open(
            `Failed to create job listing: ${error.error?.detail || 'Unknown error'}`,
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
