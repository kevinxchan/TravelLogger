import React from 'react';
import {Button, Col, Form, FormControl} from 'react-bootstrap';
import {Redirect} from 'react-router-dom';
import APIObj from '../API';
import {Formik} from 'formik';
import * as yup from "yup";

APIObj.createEntity({endpointName: 'user'});

const schema = yup.object().shape({
  username: yup.string()
    .required('Username is required')
    .min(3, 'Username must be at least 3 characters'),
  password: yup.string()
    .required('Password is required')
    .min(6, 'Password must be at least 6 characters')
});

class SignUp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      redirectToDashboard: false
    }
  }

  handleSubmit(values) {
    const payload = {
      username: values.username,
      password: values.password,
      first_name: values.firstName,
      last_name: values.lastName,
    };

    APIObj.endpoints.user.create(payload)
      .then((response) => {this.setState({redirectToDashboard: true})})
      .catch((response) => {alert('Something went wrong. Please try again.')})
  }

  render() {
    const redirectToDashboard = this.state.redirectToDashboard;
    if (redirectToDashboard === true)
      return <Redirect to={"/"}/>;

    return (
      <Formik
        validationSchema={schema}
        onSubmit={(values) => {this.handleSubmit(values)}}
        initialValues={{
          username: '',
          password: '',
          firstName: '',
          lastName: ''
        }}
      >
        {({
          handleSubmit,
          handleChange,
          touched,
          errors,
          values,
        }) => (
          <Form noValidate onSubmit={handleSubmit}>
              <Form.Group as={Col} controlId={"formGroupUsername"}>
                <Form.Label>Username</Form.Label>
                <Form.Control
                  type="username"
                  name={"username"}
                  placeholder="Enter username"
                  value={values.username}
                  onChange={handleChange}
                  isValid={touched.username && !errors.username}
                  isInvalid={!!errors.username} />
                <FormControl.Feedback type={"invalid"}>
                  {errors.username}
                </FormControl.Feedback>
              </Form.Group>

              <Form.Group as={Col} controlId={"formGroupPassword"}>
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  name={"password"}
                  placeholder="Password"
                  value={values.password}
                  onChange={handleChange}
                  isValid={touched.password && !errors.password}
                  isInvalid={!!errors.password} />
                <FormControl.Feedback type={"invalid"}>
                  {errors.password}
                </FormControl.Feedback>
              </Form.Group>

              <Form.Group as={Col} controlId={"formGroupFirstName"}>
                <Form.Label>First Name (optional)</Form.Label>
                <Form.Control
                  type="text"
                  name={"firstName"}
                  placeholder="First Name"
                  value={values.firstName}
                  onChange={handleChange} />
              </Form.Group>

              <Form.Group as={Col} controlId={"formGroupLastName"}>
                <Form.Label>Last Name (optional)</Form.Label>
                <Form.Control
                  type="text"
                  name={"lastName"}
                  placeholder="Last Name"
                  value={values.lastName}
                  onChange={handleChange} />
              </Form.Group>

            <Button
              variant="primary"
              type="submit" >
              Sign Up!
            </Button>
          </Form>
        )}
      </Formik>
    )
  }
}

export default SignUp;