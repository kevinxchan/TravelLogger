import axios from 'axios';

class API {

  constructor({url}) {
    this.url = url;
    this.endpoints = {};
  }

  createEntity(entity) {
    this.endpoints[entity.endpointName] = this.createEndpoints(entity);
  }

  createEndpoints({endpointName}) {
    const endpoints = {};
    const resourceURL = `${this.url}/${endpointName}`;

    endpoints.create = (toCreate) => {return axios.post(resourceURL, toCreate)};
    endpoints.delete = (toDelete) => {return axios.delete(resourceURL, toDelete)};
    return endpoints;
  }
}

const APIObj = new API({url: 'http://127.0.0.1:5000/api'});
export default APIObj;