__all__ = ["integrate_velocity_field"]

from .process_args import _int_antsProcessArguments
from .. import utils


def integrate_velocity_field(
    reference_image,
    velocity_field_filename,
    deformation_field=None,
    time_0=0,
    time_1=1,
    delta_time=0.01,
):
    """
    Converts a scalar image into a binary image by thresholding operations

    ANTsR function: `integrateVelocityField`

    Arguments
    ---------
    image : ANTsImage
        Input image to operate on

    low_thresh : scalar (optional)
        Lower edge of threshold window

    hight_thresh : scalar (optional)
        Higher edge of threshold window

    inval : scalar
        Output value for image voxels in between lothresh and hithresh

    outval : scalar
        Output value for image voxels lower than lothresh or higher than hithresh

    binary : boolean
        if true, returns binary thresholded image
        if false, return binary thresholded image multiplied by original image

    Returns
    -------
    ANTsImage

    Example
    -------
    >>> import ants
    >>> image = ants.image_read( ants.get_ants_data('r16') )
    >>> timage = ants.integrate_velocity_field(image, 0.5, 1e15)
    """
    args = [dim, image, outimage, low_thresh, high_thresh, inval, outval]
    processed_args = _int_antsProcessArguments(args)
    libfn = utils.get_lib_fn("ANTSIntegrateVelocityField")
    libfn(processed_args)
    if binary:
        return outimage
    else:
        return outimage * image
