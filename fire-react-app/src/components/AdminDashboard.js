import React, { useState } from 'react';
import axios from 'axios';

const AdminDashboard = () => {
    const [file, setFile] = useState(null);
    const [success, setSuccess] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!file) {
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('/admin_panel/dashboard/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.data.success) {
                setSuccess(true);
            } else {
                setSuccess(false);
            }
        } catch (err) {
            console.error(err);
            setSuccess(false);
        }
    };

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Upload CSV:
                    <input
                        type="file"
                        accept=".csv"
                        onChange={(e) => setFile(e.target.files[0])}
                    />
                </label>
                <button type="submit">Upload</button>
            </form>
            {success && <p>Data successfully updated.</p>}
        </div>
    );
};

export default AdminDashboard;
