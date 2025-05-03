/**
 * The Job Application Model defines the shape of the Model
 * used by the Backend APIs
 *
 * @author Zhi Hang Yang, Joseph Zheng, Kaw Bu, Kamal Deep Vasireddy
 * @copyright 2025
 * @license MIT
 */

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
