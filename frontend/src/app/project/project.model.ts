/**
 * The Project Model defines the shape of Project data
 * retrieved from the Project Service and the API.
 *
 * @author Kamal Deep Vasireddy, Joseph Zheng, Z, Kaw Za Thang Bu, Diddy Developer
 * @copyright 2025
 * @license MIT
 */

/** Interface for Project Type (used on frontend for projects page) */
export interface Project {
  id: number | null;
  author_id: number | null;
  author: string;
  image: string;
  title: string;
  short_description: string;
  long_description: string;
  requirements: string;
  additional_info: string;
  email: string;
  phone_number: string;
  linked_in: string;
  public: boolean;
  slug: string;
}
