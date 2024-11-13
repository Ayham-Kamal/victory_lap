"use client";
import React, { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { useRouter } from 'next/navigation';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    // Placeholder for authentication logic
    if (email === 'test@example.com' && password === 'password') {
      router.push('/dashboard');
    } else {
      setError('Invalid email or password');
    }
  };

  return (
    <div className="relative flex min-h-screen items-center justify-center bg-gray-900 bg-opacity-50 p-6">
      {/* Background Image */}
      <div className="absolute inset-0">
        <Image
          src="/loginBackground.jpg"
          alt="Background Image"
          layout="fill"
          objectFit="cover"
          className="z-0"
        />
      </div>

      {/* Login Form Container */}
      <div className="relative w-full max-w-md backdrop-blur-sm bg-white bg-opacity-20 rounded-lg shadow-lg p-8 space-y-6 z-10">
      
        <div className="text-center">
        <h1 className="text-2xl font-bold text-white">Login</h1>
          <Image
            src="/logo.png"
            alt="Fitness App Logo"
            width={300}
            height={100}
            className="mx-auto mb-4"
          />
        </div>
        <form onSubmit={handleSubmit} className="space-y-4">
          {error && <p className="text-red-500 text-sm">{error}</p>}
          <div>
            <label className="block text-sm font-medium text-white">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none bg-white bg-opacity-50 placeholder-gray-300"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-white">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="mt-1 block w-full p-2 border border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none bg-white bg-opacity-50 placeholder-gray-300"
              required
            />
          </div>
          <button
            type="submit"
            className="w-full bg-blue-500 text-white font-semibold p-2 rounded-lg hover:bg-blue-600 transition-colors"
          >
            Login
          </button>
        </form>
        <div className="text-center">
          <p className="text-gray-200 text-sm">
            Dont have an account?{' '}
            <Link href="/signup" className="text-blue-300 hover:underline">
              Sign up
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
