import { Pipe, PipeTransform } from '@angular/core';
import { Project } from '../project.model';

@Pipe({
  name: 'projectFilter'
})
export class ProjectFilterPipe implements PipeTransform {
  /** Returns a mapped array of projects that start with the input string (if search query provided).
   * @param {Observable<Project[]>} projects: observable list of valid Project models
   * @param {String} searchQuery: input string to filter by
   * @returns {Observable<Project[]>}
   */
  transform(projects: Project[], searchQuery: String): Project[] {
    // Sort the projects list alphabetically by name
    projects = projects.sort((a: Project, b: Project) => {
      return a.title.toLowerCase().localeCompare(b.title.toLowerCase());
    });

    // If a search query is provided, return the projects that start with the search query.
    if (searchQuery) {
      return projects.filter(
        (project) =>
          project.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
          project.short_description
            .toLowerCase()
            .includes(searchQuery.toLowerCase()) ||
          project.long_description
            .toLowerCase()
            .includes(searchQuery.toLowerCase())
      );
    } else {
      // Otherwise, return the original list.
      return projects;
    }
  }
}
