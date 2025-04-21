import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

/* Angular Material Modules */
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card';
import { MatTabsModule } from '@angular/material/tabs';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatListModule } from '@angular/material/list';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatTooltipModule } from '@angular/material/tooltip';

import { ProjectRoutingModule } from './project-routing.module';
import { ProjectPageComponent } from './project-page/project-page.component';
import { ProjectCard } from './widgets/project-card/project-card.widget';
import { ProjectDetailsInfoCard } from './widgets/project-details-info-card/project-details-info-card.widget';
import { RouterModule } from '@angular/router';
import { SharedModule } from '../shared/shared.module';
import { ProjectDetailsComponent } from './project-details/project-details.component';
import { AISearchBar } from './widgets/ai-search-bar/ai-search-bar.widget';
import{ AiResumeSearch } from "./widgets/ai-resume-search/ai-resume-search.widget"

@NgModule({
  declarations: [
    ProjectDetailsComponent,
    ProjectPageComponent,
    ProjectCard,
    ProjectDetailsInfoCard,
    AISearchBar,
    AiResumeSearch,
  ],
  imports: [
    CommonModule,
    MatTabsModule,
    MatTableModule,
    MatCardModule,
    MatDialogModule,
    MatButtonModule,
    MatSelectModule,
    MatFormFieldModule,
    MatInputModule,
    MatPaginatorModule,
    MatListModule,
    MatAutocompleteModule,
    FormsModule,
    ReactiveFormsModule,
    MatIconModule,
    MatTooltipModule,
    ProjectRoutingModule,
    RouterModule,
    SharedModule,
  ]
})
export class ProjectModule {}
