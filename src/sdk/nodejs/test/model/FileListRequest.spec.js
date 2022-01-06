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
    describe('FileListRequest', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.FileListRequest();
      });

      it('should create an instance of FileListRequest', function() {
        // TODO: update the code to test FileListRequest
        expect(instance).to.be.a(SelfManagedOsdu.FileListRequest);
      });

      it('should have the property timeFrom (base name: "TimeFrom")', function() {
        // TODO: update the code to test the property timeFrom
        expect(instance).to.have.property('timeFrom');
        // expect(instance.timeFrom).to.be(expectedValueLiteral);
      });

      it('should have the property timeTo (base name: "TimeTo")', function() {
        // TODO: update the code to test the property timeTo
        expect(instance).to.have.property('timeTo');
        // expect(instance.timeTo).to.be(expectedValueLiteral);
      });

      it('should have the property pageNum (base name: "PageNum")', function() {
        // TODO: update the code to test the property pageNum
        expect(instance).to.have.property('pageNum');
        // expect(instance.pageNum).to.be(expectedValueLiteral);
      });

      it('should have the property items (base name: "Items")', function() {
        // TODO: update the code to test the property items
        expect(instance).to.have.property('items');
        // expect(instance.items).to.be(expectedValueLiteral);
      });

      it('should have the property userID (base name: "UserID")', function() {
        // TODO: update the code to test the property userID
        expect(instance).to.have.property('userID');
        // expect(instance.userID).to.be(expectedValueLiteral);
      });

    });
  });

}));