variable "cidr" {
    default = "10.0.0.0/16"
}

variable "az" {
    default = "ap-south-1a"  
}

variable "sub_cidr" {
    default = "10.0.1.0/24"
}

variable "vpc_name" {
    default = "vpc_face_recog"
}

variable "sub_name" {
    default = "subnet_name_face_recog"
}

variable "gw_name" {
    default = "gw_name_face_recog"
}

variable "rt_name" {
    default = "rt_name_face_recog"
}