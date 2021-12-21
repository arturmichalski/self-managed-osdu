/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.22
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/PartitionProperty'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./PartitionProperty'));
  } else {
    // Browser globals (root is window)
    if (!root.SelfManagedOsdu) {
      root.SelfManagedOsdu = {};
    }
    root.SelfManagedOsdu.PartitionDto = factory(root.SelfManagedOsdu.ApiClient, root.SelfManagedOsdu.PartitionProperty);
  }
}(this, function(ApiClient, PartitionProperty) {
  'use strict';

  /**
   * The PartitionDto model module.
   * @module model/PartitionDto
   * @version 0.11.0
   */

  /**
   * Constructs a new <code>PartitionDto</code>.
   * @alias module:model/PartitionDto
   * @class
   * @param properties {Object.<String, module:model/PartitionProperty>} Free form key value pair object for any data partition specific values
   */
  var exports = function(properties) {
    this.properties = properties;
  };

  /**
   * Constructs a <code>PartitionDto</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PartitionDto} obj Optional instance to populate.
   * @return {module:model/PartitionDto} The populated <code>PartitionDto</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('properties'))
        obj.properties = ApiClient.convertToType(data['properties'], {'String': PartitionProperty});
    }
    return obj;
  }

  /**
   * Free form key value pair object for any data partition specific values
   * @member {Object.<String, module:model/PartitionProperty>} properties
   */
  exports.prototype.properties = undefined;


  return exports;

}));
