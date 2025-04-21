import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';
import { Project } from './project.model';
import { catchError, map, of } from 'rxjs';
import { ProjectService } from './project.service';

export const projectResolver: ResolveFn<Project | undefined> = (
  route,
  _state
) => {
  //   if (route.paramMap.get('slug')! == 'new') {
  //     return {
  //       id: null,
  //       author: '',
  //       image: '',
  //       title: '',
  //       short_description: '',
  //       long_description: '',
  //       requirements: '',
  //       additional_info: '',
  //       email: '',
  //       phone_number: '',
  //       linked_in: '',
  //       public: false,
  //       slug: ''
  //     };
  //   }

  return inject(ProjectService)
    .getProject(route.paramMap.get('slug')!)
    .pipe(
      catchError((error) => {
        console.log(error);
        return of(undefined);
      })
    );
};
