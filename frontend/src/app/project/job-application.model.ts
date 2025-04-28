export interface JobApplication {
  id: number | null;
  user_id: number;
  poster_id: number;
  project_id: number;
  personal_statement: string;
  experience: string;
  gpa: number;
  skills: string;
  contact: string;
}
