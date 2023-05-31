(define (batch-lighten pattern)
  (let* ((filelist (cadr (file-glob pattern 1))))
    (while (not (null? filelist))
           (let* ((filename (car filelist))
                  (image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
                  (drawable (car (gimp-image-get-active-layer image))))
             ; lighten colors
             (gimp-brightness-contrast drawable 60 0)
             ; save result
             (let* ((new-filename (string-append (substring filename 0 (- (string-length filename) 4)) "_light.png")))
               (gimp-file-save RUN-NONINTERACTIVE image drawable new-filename new-filename))
             ; delete image from memory
             (gimp-image-delete image))
           ; process next file
           (set! filelist (cdr filelist)))))
