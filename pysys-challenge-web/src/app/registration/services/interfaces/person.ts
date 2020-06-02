import {Timestamp} from 'rxjs';

export interface Person {
  name: string;
  email: string;
  registrationDate: Timestamp<string>;
}
