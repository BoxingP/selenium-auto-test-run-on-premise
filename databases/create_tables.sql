CREATE TABLE selenium_test_steps (
    id serial primary key not null,
    case_id varchar not null,
    steps varchar not null,
    time timestamp not null,
    duration float not null,
    status_id int4 not null,
    CONSTRAINT fk_status_steps FOREIGN KEY(status_id) REFERENCES status_of_failure(id)
);

CREATE TABLE selenium_test_availability (
    id serial primary key not null,
    case_id varchar not null,
    time timestamp not null,
    availability int4 not null
);