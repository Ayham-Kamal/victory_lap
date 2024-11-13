"use client";
import React, { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Image from "next/image";

const SignUpPage = () => {
  const router = useRouter();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [errors, setErrors] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const validateForm = () => {
    const newErrors = { ...errors };
    let isValid = true;

    if (!formData.name) {
      newErrors.name = "Name is required.";
      isValid = false;
    } else {
      newErrors.name = "";
    }

    if (!formData.email) {
      newErrors.email = "Email is required.";
      isValid = false;
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Email is invalid.";
      isValid = false;
    } else {
      newErrors.email = "";
    }

    if (!formData.password) {
      newErrors.password = "Password is required.";
      isValid = false;
    } else if (formData.password.length < 6) {
      newErrors.password = "Password must be at least 6 characters.";
      isValid = false;
    } else {
      newErrors.password = "";
    }

    if (formData.confirmPassword !== formData.password) {
      newErrors.confirmPassword = "Passwords do not match.";
      isValid = false;
    } else {
      newErrors.confirmPassword = "";
    }

    setErrors(newErrors);
    return isValid;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (validateForm()) {
      // TODO: Send data to the server for sign-up
      console.log("User signed up:", formData);
      router.push("/dashboard"); // Navigate to dashboard after successful signup
    }
  };

  return (
    <div
      className="flex flex-col items-center justify-center min-h-screen py-2 bg-cover bg-center"
      style={{
        backgroundImage: "url('CrossFit.jpg')",
        // filter: "blur(1px)", // Apply blur to background image
      }}
    >
      <div className="relative flex flex-col items-center justify-center min-h-screen w-full bg-black bg-opacity-40">
        <div className="bg-white bg-opacity-85 rounded-lg shadow-2xl p-8 w-full max-w-md">
          {/* <h1 className="text-3xl font-bold text-center text-gray-900 mb-6">
            Sign Up for Victory Lap
          </h1> */}
        <div className="text-center">
        <h1 className="text-3xl font-bold text-center text-gray-900 mb-6">Sign Up</h1>
          <Image
            src="/logo.png"
            alt="Fitness App Logo"
            width={300}
            height={100}
            className="mx-auto mb-4"
            />
        </div>
          <form onSubmit={handleSubmit} className="flex flex-col">
            <label className="font-semibold text-gray-700 mb-2">Name</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              className="mb-4 p-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.name && (
              <p className="text-red-500 text-sm">{errors.name}</p>
            )}

            <label className="font-semibold text-gray-700 mb-2">Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="mb-4 p-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.email && (
              <p className="text-red-500 text-sm">{errors.email}</p>
            )}

            <label className="font-semibold text-gray-700 mb-2">Password</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="mb-4 p-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.password && (
              <p className="text-red-500 text-sm">{errors.password}</p>
            )}

            <label className="font-semibold text-gray-700 mb-2">
              Confirm Password
            </label>
            <input
              type="password"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              className="mb-4 p-2 border border-gray-300 rounded shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {errors.confirmPassword && (
              <p className="text-red-500 text-sm">{errors.confirmPassword}</p>
            )}

            <button
              type="submit"
              className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700 shadow-md"
            >
              Sign Up
            </button>
          </form>
          <p className="mt-4 text-center text-gray-800">
            Already have an account?{" "}
            <Link href="/login" className="text-blue-600 hover:underline">
              Log In
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignUpPage;
