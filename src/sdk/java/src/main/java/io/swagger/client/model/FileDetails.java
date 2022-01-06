/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.FileExtensionProperties;
import io.swagger.client.model.FileMetaItem;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Further information about File being uploaded.
 */
@ApiModel(description = "Further information about File being uploaded.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2022-01-06T20:30:18.662Z")
public class FileDetails {
  @SerializedName("TargetKind")
  private String targetKind = null;

  @SerializedName("FileType")
  private String fileType = null;

  @SerializedName("FrameOfReference")
  private List<FileMetaItem> frameOfReference = null;

  @SerializedName("ExtensionProperties")
  private FileExtensionProperties extensionProperties = null;

  @SerializedName("ParentReference")
  private String parentReference = null;

  public FileDetails targetKind(String targetKind) {
    this.targetKind = targetKind;
    return this;
  }

   /**
   * The target kind or schema ID which is to be used by the parser.
   * @return targetKind
  **/
  @ApiModelProperty(example = "os:npd:wellbore:1:*.*", value = "The target kind or schema ID which is to be used by the parser.")
  public String getTargetKind() {
    return targetKind;
  }

  public void setTargetKind(String targetKind) {
    this.targetKind = targetKind;
  }

  public FileDetails fileType(String fileType) {
    this.fileType = fileType;
    return this;
  }

   /**
   * Type of File to decide what kind of ingestion to be triggered
   * @return fileType
  **/
  @ApiModelProperty(example = "csv", value = "Type of File to decide what kind of ingestion to be triggered")
  public String getFileType() {
    return fileType;
  }

  public void setFileType(String fileType) {
    this.fileType = fileType;
  }

  public FileDetails frameOfReference(List<FileMetaItem> frameOfReference) {
    this.frameOfReference = frameOfReference;
    return this;
  }

  public FileDetails addFrameOfReferenceItem(FileMetaItem frameOfReferenceItem) {
    if (this.frameOfReference == null) {
      this.frameOfReference = new ArrayList<FileMetaItem>();
    }
    this.frameOfReference.add(frameOfReferenceItem);
    return this;
  }

   /**
   * The list metaItem definitions which maps a named frame of reference symbol or name to the self-contained persistableReference.
   * @return frameOfReference
  **/
  @ApiModelProperty(value = "The list metaItem definitions which maps a named frame of reference symbol or name to the self-contained persistableReference.")
  public List<FileMetaItem> getFrameOfReference() {
    return frameOfReference;
  }

  public void setFrameOfReference(List<FileMetaItem> frameOfReference) {
    this.frameOfReference = frameOfReference;
  }

  public FileDetails extensionProperties(FileExtensionProperties extensionProperties) {
    this.extensionProperties = extensionProperties;
    return this;
  }

   /**
   * Get extensionProperties
   * @return extensionProperties
  **/
  @ApiModelProperty(value = "")
  public FileExtensionProperties getExtensionProperties() {
    return extensionProperties;
  }

  public void setExtensionProperties(FileExtensionProperties extensionProperties) {
    this.extensionProperties = extensionProperties;
  }

  public FileDetails parentReference(String parentReference) {
    this.parentReference = parentReference;
    return this;
  }

   /**
   * The parent reference for this file.
   * @return parentReference
  **/
  @ApiModelProperty(example = "CSBE0417", value = "The parent reference for this file.")
  public String getParentReference() {
    return parentReference;
  }

  public void setParentReference(String parentReference) {
    this.parentReference = parentReference;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FileDetails fileDetails = (FileDetails) o;
    return Objects.equals(this.targetKind, fileDetails.targetKind) &&
        Objects.equals(this.fileType, fileDetails.fileType) &&
        Objects.equals(this.frameOfReference, fileDetails.frameOfReference) &&
        Objects.equals(this.extensionProperties, fileDetails.extensionProperties) &&
        Objects.equals(this.parentReference, fileDetails.parentReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(targetKind, fileType, frameOfReference, extensionProperties, parentReference);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FileDetails {\n");
    
    sb.append("    targetKind: ").append(toIndentedString(targetKind)).append("\n");
    sb.append("    fileType: ").append(toIndentedString(fileType)).append("\n");
    sb.append("    frameOfReference: ").append(toIndentedString(frameOfReference)).append("\n");
    sb.append("    extensionProperties: ").append(toIndentedString(extensionProperties)).append("\n");
    sb.append("    parentReference: ").append(toIndentedString(parentReference)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

