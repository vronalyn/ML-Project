function confirmDelete(id) {
        // Use SweetAlert to confirm the delete action
        Swal.fire({
            title: 'Are you sure you want to delete the record?',
            text: 'This action cannot be undone!',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Delete',
            cancelButtonText: 'Cancel'
        }).then((result) => {
            if (result.isConfirmed) {
                // If confirmed, redirect to the delete URL (e.g., /delete/id)
                window.location.href = '/prediction/';
            }
        });
    }
