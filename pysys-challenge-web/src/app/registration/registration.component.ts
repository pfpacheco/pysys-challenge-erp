import { Component, OnInit } from '@angular/core';

import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

import { Person } from './services/interfaces/person';
import { RegistrationService } from './services/registration.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  registrationGroup: FormGroup;
  person: Person;

  constructor(
    private formBuilder: FormBuilder,
    private registrationService: RegistrationService
  ) { }

  ngOnInit(): void {
    this.registrationGroup = this.formBuilder.group({
      name: ['', [
          Validators.required,
          Validators.maxLength(12),
        ]
      ],
      username: ['', []],
      email: ['', []],
      password: ['', []],
      confirm_password: ['', []]
    });
  }
  ngOnSubmit(): void {
  }
}
