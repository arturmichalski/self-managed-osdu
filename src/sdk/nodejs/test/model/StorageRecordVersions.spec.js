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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SelfManagedOsdu);
  }
}(this, function(expect, SelfManagedOsdu) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('StorageRecordVersions', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.StorageRecordVersions();
      });

      it('should create an instance of StorageRecordVersions', function() {
        // TODO: update the code to test StorageRecordVersions
        expect(instance).to.be.a(SelfManagedOsdu.StorageRecordVersions);
      });

      it('should have the property recordId (base name: "recordId")', function() {
        // TODO: update the code to test the property recordId
        expect(instance).to.have.property('recordId');
        // expect(instance.recordId).to.be(expectedValueLiteral);
      });

      it('should have the property versions (base name: "versions")', function() {
        // TODO: update the code to test the property versions
        expect(instance).to.have.property('versions');
        // expect(instance.versions).to.be(expectedValueLiteral);
      });

    });
  });

}));
